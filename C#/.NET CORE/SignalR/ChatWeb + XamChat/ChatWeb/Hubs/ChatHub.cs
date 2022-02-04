using Microsoft.AspNetCore.SignalR;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ChatWeb.Hubs
{
    public class ChatHub:Hub
    {
        public async Task SendMessage(string user, string message)
        //public async Task SendMessage(string user, string message, string group)
        {
            //**********EL HUB recibi la peticion y la distribuye  alos clientes****************//
            //**********  Desde javascrit  -------> C# -----------> View Javascript*****************//

            //CONFIG:
            // Registrar en Startup: Debajo de,=============>   public void ConfigureServices(I...
            // poner =======>  services.AddSignalR();
            /* Tambien en Startup: arriba de appUseMVc =================>   app.UseSignalR(x =>
                                                                          {
                                                                              x.MapHub<nombre de class del hub>("/url del hub");
                                                                          });*/
            // proyecto >> npm init -y
            // proyecto >> npm i @aspnet/signalr
            /* Cortar y Pegar:
             *   -  buscar el archivo y corta, signalr.js   =======> en: C:\Proyectos\ChatWeb\node_modules\@aspnet\signalr\dist\browser
             *     
             *     Y pegar: hacer una carpeta signalR y pegar dentro ==============> C:\Proyectos\ChatWeb\ChatWeb\wwwroot\lib\signalR\signalr.js
                 
                 -   Y poner esto en View =======>  script src="~/lib/signalR/signalr.js"></script>
                                                   <script src="~/js/chat.js" ></script>
             
             */

            //await Clients.Group(group).SendAsync("ReceiveMessage", user, message);




            await Clients.All.SendAsync("ReceiveMessage", user, message);

        }
     }
 }
