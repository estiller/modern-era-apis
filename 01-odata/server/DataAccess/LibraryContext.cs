using Microsoft.EntityFrameworkCore;
using ModernEraApis.OData.Server.Model;

namespace ModernEraApis.OData.Server.DataAccess
{
    public class LibraryContext : DbContext
    {
        public DbSet<Book> Books { get; set; } = null!;
        public DbSet<User> Users { get; set; } = null!;

        public LibraryContext(DbContextOptions<LibraryContext> options) : base(options)
        {
        }

        protected override void OnModelCreating(ModelBuilder builder)
        {
            builder.Entity<Book>().HasOne(book => book.Borrower!);

            SeedData(builder);
        }

        private void SeedData(ModelBuilder builder)
        {
            builder.Entity<User>().HasData(
                new User { Id = 1, Name = "John" },
                new User { Id = 2, Name = "Mary" },
                new User { Id = 3, Name = "Alice" });

            builder.Entity<Book>().HasData(
                new Book { Id = 1, Name = "The Hitchhiker's Guide to the Galaxy"},
                new Book { Id = 2, Name = "The Restaurant at the End of the Universe"},
                new Book { Id = 3, Name = "Life, the Universe and Everything"},
                new Book { Id = 4, Name = "So Long, and Thanks for All the Fish"},
                new Book { Id = 5, Name = "Mostly Harmless"});
        }
    }
}