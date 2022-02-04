using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(ChatStrap.Startup))]
namespace ChatStrap
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
            app.MapSignalR();
        }
    }
}
