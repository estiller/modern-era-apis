namespace ModernEraApis.OData.Server.Model
{
    public class Book
    {
        public int Id { get; set; }
        public string Name { get; set; } = null!;
        public User? Borrower { get; set; }
    }
}