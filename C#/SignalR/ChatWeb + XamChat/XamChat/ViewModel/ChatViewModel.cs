using MvvmHelpers;
using Xamarin.Forms;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Text;
using XamChat.Model;
using Microsoft.AspNetCore.SignalR.Client;
using System.Threading.Tasks;
using System.Linq.Expressions;

namespace XamChat.ViewModel
{
 /* INSTALAR EN NUGET:
       - MicrosoftAspNetCore.Client
       - Reafatured.mvvmHelpers */

    public class ChatViewModel:BaseViewModel
    {
        HubConnection hubConnection;

        public ChatMessage ChatMessage { get; } 

        public ObservableRangeCollection<ChatMessage> Messages { get; }

        public Command SendMessageCommand { get; }
        public Command ConnectCommand { get; }
        public Command DisconnectCommand { get; }

        Random random;
        bool isConnected;
        public bool IsConnected
        {
            get => isConnected;
            set
            {
                Device.BeginInvokeOnMainThread(() =>
                {
                    SetProperty(ref isConnected, value);
                });
            }
        }

        public ChatViewModel()
        {

            ChatMessage = new ChatMessage();
            Messages = new ObservableRangeCollection<ChatMessage>();
            SendMessageCommand = new Command(async () => await SendMessage());
            ConnectCommand = new Command(async () => await Connect());
            DisconnectCommand = new Command(async () => await Disconnect());

            random = new Random();

            hubConnection = new HubConnectionBuilder()
                            .WithUrl("http://flutterchat.somee.com/chatHub")
                            .Build();

          

            hubConnection.Closed += async (error) =>
            {
                SendLocalMesssage("Close siganR.....");
                IsConnected = false;
                await Task.Delay(random.Next(0, 5) * 1000);
                await Connect();
            };

            hubConnection.On<string, string>("ReceiveMessage", (user, message) => {
                
                var finalMessage =  $"{ user } say  { message }";
                SendLocalMesssage(finalMessage);

            });

            }


        async Task Connect()
        {
            if (IsConnected)
                return;
           try
            {
                await hubConnection.StartAsync();
                IsConnected = true;

                Messages.Add(new ChatMessage
                {
                    Message = "Connected..."
                });
            }
           catch(Exception ex)    
            {
                Messages.Add(new ChatMessage
                {
                    Message = $"Connected error:{ex.Message}"
                });
            }
        }

        async Task Disconnect()
        {
            if (!IsConnected)
                return;

            await hubConnection.StopAsync();
            IsConnected = false;
            SendLocalMesssage("Disconnect....");
        }

        async Task SendMessage()
        {
            try
            {
                await hubConnection.InvokeAsync("SendMessage",
                                                ChatMessage.User,
                                                ChatMessage.Message);
            }
            catch(Exception ex)
            {
                SendLocalMesssage($"Send error:{ex.Message}");
            }
        }


        private void SendLocalMesssage(string message)
        {
           Device.InvokeOnMainThreadAsync(() =>
           {
               Messages.Add(new ChatMessage
               {
                   Message = message
               });

           });
            
        }
    }

   
}
    
