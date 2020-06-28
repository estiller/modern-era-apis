using System;
using ModernEraApis.AsyncApi.Server.Messaging.Events;
using Saunter.Attributes;

namespace ModernEraApis.AsyncApi.Server.Messaging
{

    [AsyncApi]
    public class LibraryMessageBus
    {
        [Channel("publish/book/transaction")]
        [PublishOperation(typeof(BookTransactionCommand), OperationId = "PublishBookTransactionCommand")]
        public void ProcessTransactionCommand(BookTransactionCommand command)
        {
            throw new NotImplementedException();
        }

        [Channel("subscribe/book/inventory")]
        [SubscribeOperation(typeof(BookInventoryUpdate), OperationId = "SubscribeBookInventoryUpdates")]
        public void PublishBookInventoryUpdate()
        {
            throw new NotImplementedException();
        }
    }
}