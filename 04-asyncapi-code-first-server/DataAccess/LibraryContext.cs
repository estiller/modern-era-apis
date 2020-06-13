using Microsoft.EntityFrameworkCore;
using ModernEraApis.AsyncApi.Server.Model;

namespace ModernEraApis.AsyncApi.Server.DataAccess
{
    public class LibraryContext : DbContext
    {
        public DbSet<Book> Books { get; set; } = null!;

        public LibraryContext(DbContextOptions<LibraryContext> options) : base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            SeedData(builder);
        }

        private void SeedData(ModelBuilder builder)
        {
            builder.Entity<Book>().HasData(
                new Book { Id = 1, Name = "The Hitchhiker's Guide to the Galaxy", Quantity = 7},
                new Book { Id = 2, Name = "The Restaurant at the End of the Universe", Quantity = 9},
                new Book { Id = 3, Name = "Life, the Universe and Everything", Quantity = 2},
                new Book { Id = 4, Name = "So Long, and Thanks for All the Fish", Quantity = 5},
                new Book { Id = 5, Name = "Mostly Harmless", Quantity = 4});
        }
    }
}