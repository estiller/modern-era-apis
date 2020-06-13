using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.AspNet.OData.Extensions;
using Microsoft.AspNetCore.Http;
using Microsoft.OData.UriParser;

namespace ModernEraApis.OData.Server.Extensions
{
    internal static class HttpRequestExtensions
    {
        public static TKey GetKeyFromUri<TKey>(this HttpRequest request, Uri uri)
        {
            if (uri == null)
            {
                throw new ArgumentNullException("uri");
            }

            var urlHelper = request.GetUrlHelper();
            var pathHandler = request.GetPathHandler();
            string serviceRoot = urlHelper.CreateODataLink(request.ODataFeature().RouteName,
                pathHandler, new List<ODataPathSegment>());
            var odataPath = pathHandler.Parse(serviceRoot, uri.AbsoluteUri, request.GetRequestContainer());

            var keySegment = odataPath.Segments.OfType<KeySegment>().LastOrDefault();
            if (keySegment == null)
            {
                throw new InvalidOperationException("The link does not contain a key.");
            }

            return (TKey)keySegment.Keys.Last().Value;
        }
    }
}