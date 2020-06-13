namespace ModernEraApis.AsyncApi.Server.Messaging.Events
{
    public class BookInventoryUpdate
    {
        public BookInventoryUpdate(int id, string name, int quantity)
        {
            Id = id;
            Name = name;
            Quantity = quantity;
        }

        public int Id { get; set; }
        public string Name { get; set; }
        public int Quantity { get; set; }
    }
}