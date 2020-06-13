using Microsoft.AspNet.OData.Builder;
using Microsoft.AspNet.OData.Extensions;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.OData.Edm;
using ModernEraApis.OData.Server.DataAccess;
using ModernEraApis.OData.Server.Model;

namespace ModernEraApis.OData.Server
{
    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddOData();
            services.AddDbContext<LibraryContext>(opts => opts.UseInMemoryDatabase("LibraryDB"));
            services.AddControllers();
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseHttpsRedirection();
            app.UseRouting();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapODataRoute("odata", "odata", GetEdmModel());
                endpoints.Count().Filter().OrderBy().Expand().Select().MaxTop(null);
            });
            CreateDatabase(app);
        }

        private static IEdmModel GetEdmModel()
        {
            var builder = new ODataConventionModelBuilder();
            builder.EntitySet<Book>("Books");
            builder.EntitySet<User>("Users");
            return builder.GetEdmModel();
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
