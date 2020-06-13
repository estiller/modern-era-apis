namespace ModernEraApis.AsyncApi.Server.Model
{
    public class Book
    {
        public int Id { get; set; }
        public string Name { get; set; } = null!;
        public int Quantity { get; set; }
    }
}