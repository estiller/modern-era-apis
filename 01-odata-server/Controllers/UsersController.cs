using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNet.OData;
using Microsoft.AspNetCore.Mvc;
using ModernEraApis.OData.Server.DataAccess;
using ModernEraApis.OData.Server.Model;

namespace ModernEraApis.OData.Server.Controllers
{
    public class UsersController : ODataController
    {
        private readonly LibraryContext _context;

        public UsersController(LibraryContext context)
        {
            _context = context;
        }

        [EnableQuery]
        public IQueryable<User> GetUsers()
        {
            return _context.Users;
        }

        [EnableQuery]
        public SingleResult<User> GetUser([FromODataUri] int key)
        {
            IQueryable<User> result = _context.Users.Where(p => p.Id == key);
            return SingleResult.Create(result);
        }

        public async Task<IActionResult> PostUser(User user)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }
            _context.Users.Add(user);
            await _context.SaveChangesAsync();
            return Created(user);
        }
    }
}
