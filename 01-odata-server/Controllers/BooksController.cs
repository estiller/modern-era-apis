using System;
using System.Linq;
using System.Net;
using System.Threading.Tasks;
using Microsoft.AspNet.OData;
using Microsoft.AspNet.OData.Extensions;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ModernEraApis.OData.Server.DataAccess;
using ModernEraApis.OData.Server.Extensions;
using ModernEraApis.OData.Server.Model;

namespace ModernEraApis.OData.Server.Controllers
{
    public class BooksController : ODataController
    {
        private readonly LibraryContext _context;

        public BooksController(LibraryContext context)
        {
            _context = context;
        }

        [EnableQuery]
        public IQueryable<Book> GetBooks()
        {
            return _context.Books;
        }

        [EnableQuery]
        public SingleResult<Book> GetBook([FromODataUri] int key)
        {
            IQueryable<Book> result = _context.Books.Where(p => p.Id == key);
            return SingleResult.Create(result);
        }

        public async Task<IActionResult> PostBook(Book book)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            _context.Books.Add(book);
            await _context.SaveChangesAsync();
            return Created(book);
        }

        [EnableQuery]
        public SingleResult<User?> GetBorrower([FromODataUri] int key)
        {
            var result = _context.Books.Where(book => book.Id == key).Select(book => book.Borrower);
            return SingleResult.Create(result);
        }

        public async Task<IActionResult> CreateRef([FromODataUri] int key, string navigationProperty, [FromBody] Uri link)
        {
            var book = await _context.Books.SingleOrDefaultAsync(book => book.Id == key);
            if (book == null)
            {
                return NotFound();
            }
            switch (navigationProperty)
            {
                case nameof(Book.Borrower):
                    var relatedKey = Request.GetKeyFromUri<int>(link);
                    var borrower = await _context.Users.SingleOrDefaultAsync(user => user.Id == relatedKey);
                    if (borrower == null)
                    {
                        return NotFound();
                    }

                    book.Borrower = borrower;
                    break;

                default:
                    return StatusCode((int)HttpStatusCode.NotImplemented);
            }
            await _context.SaveChangesAsync();
            return NoContent();
        }
    }
}
