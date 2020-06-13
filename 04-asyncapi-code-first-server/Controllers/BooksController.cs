using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using ModernEraApis.AsyncApi.Server.DataAccess;
using ModernEraApis.AsyncApi.Server.Model;

namespace ModernEraApis.AsyncApi.Server.Controllers
{

    [ApiController]
    [Route("api/books")]
    public class BooksController : ControllerBase
    {
        private readonly LibraryContext _context;

        public BooksController(LibraryContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IEnumerable<Book> GetBooks()
        {
            return _context.Books;
        }
    }
}
