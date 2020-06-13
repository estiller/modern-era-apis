namespace ModernEraApis.AsyncApi.Server.Messaging.Events
{
    public class BookTransactionCommand
    {
        public int Id { get; set; }
        public TransactionType TransactionType { get; set; }
    }
}