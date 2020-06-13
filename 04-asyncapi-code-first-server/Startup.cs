using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using ModernEraApis.AsyncApi.Server.DataAccess;
using ModernEraApis.AsyncApi.Server.Messaging;
using Saunter;
using Saunter.AsyncApiSchema.v2;
using Saunter.Generation;

namespace ModernEraApis.AsyncApi.Server
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        public void ConfigureServices(IServiceCollection services)
        {
            services.AddDbContext<LibraryContext>(opts => opts.UseInMemoryDatabase("LibraryDB"));

            services.AddControllers();

            services.AddAsyncApiSchemaGeneration(options =>
            {
                options.AssemblyMarkerTypes = new[] { typeof(LibraryMessageBus) };

                options.AsyncApi = new AsyncApiDocument
                {
                    Info = new Info("Library API", "1.0.0")
                    {
                        Description = "The Library API allows you to remotely add books to the library.",
                        License = new License("MIT")
                        {
                            Url = "https://github.com/estiller/modern-era-apis/blob/master/LICENSE"
                        }
                    },
                    Servers =
                    {
                        { "production", new Saunter.AsyncApiSchema.v2.Server("mqtt://test.mosquitto.org", "mqtt") }
                    }
                };
            });
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseRouting();

            app.UseAuthorization();

            app.UseMiddleware<AsyncApiMiddleware>();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });

            CreateDatabase(app);
        }

        private static void CreateDatabase(IApplicationBuilder app)
        {
            using (var serviceScope = app.ApplicationServices
                .GetRequiredService<IServiceScopeFactory>()
                .CreateScope())
            {
                using (var context = serviceScope.ServiceProvider.GetService<LibraryContext>())
                {
                    context.Database.EnsureCreated();
                }
            }
        }
    }
}
