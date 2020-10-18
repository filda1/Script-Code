using Microsoft.AspNetCore.SignalR.Client;
using MvvmHelpers;
using MvvmHelpers.Commands;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Essentials;
using Xamarin.Forms;
using XamarinSignalRapp.Model;
using Command = Xamarin.Forms.Command;


/// <summary>
/// /Ver Videos Youtube y Github de James Montemagno
/// POST =========> http://www.xamarinsignalr.somee.com/api/v1/signals/deliverypoint
/// </summary>
namespace XamarinSignalRapp.ViewModel
{
    public class DataMessageViewModel : BaseViewModel
    {
        HubConnection hubConnection;

        public Message ServerMessage { get; }
        public Data Data { get; }


        public ObservableRangeCollection<Message> Messages { get; }

        public ObservableRangeCollection<Data> Datas { get; }

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



        public DataMessageViewModel()
        {
            ServerMessage = new Message();
            Data = new Data();

            Messages = new ObservableRangeCollection<Message>();
            Datas = new ObservableRangeCollection<Data>();

            SendMessageCommand = new Command(async () => await SendMessage());
            ConnectCommand = new Command(async () => await Connect());
            DisconnectCommand = new Command(async () => await Disconnect());

            random = new Random();

            //HUB
            hubConnection = new HubConnectionBuilder()
                            .WithUrl("http://xamarinsignalr.somee.com/signalHub")
                            .Build();


            hubConnection.Closed += async (error) =>
            {
                SendLocalMesssage("Close siganR.....");
                IsConnected = false;
                await Task.Delay(random.Next(0, 5) * 1000);
                await Connect();
            };



            hubConnection.On<Data>("SignalMessageReceived", (signalViewModel) => {
                MainThread.BeginInvokeOnMainThread(() =>
                {

                    Datas.Insert(0, new Data
                    {
                        Description = signalViewModel.Description,
                        CustomerName= signalViewModel.CustomerName,
                        Area = signalViewModel.Area,
                        Zone =signalViewModel.Zone,
                        SignalStamp = signalViewModel.SignalStamp
                    });

                        Console.WriteLine(signalViewModel);
                                 

                });

            });



            /*hubConnection.On<string>("SignalMessageReceived", (signalViewModel) => {
                MainThread.BeginInvokeOnMainThread(() =>
                 {
                     try
                     {
                         var newItem = JsonConvert.DeserializeObject<Data>(signalViewModel);
                         Datas.Insert(0, newItem);

                         Console.WriteLine(signalViewModel);
                     }
                     catch (Exception ex)
                     {
                       Messages.Add(new Message
                        {
                        ServerMessage = $"Connected error:{ex.Message}"
                        });

                     }   

               });

            });*/


            //FUNCIONA
            /*hubConnection.On<string, string, string, string>("SignalMessageReceived", (user, message, date, zone) => {

                var finalMessage = $"{ user } say  { message } now  { date } from  { zone }";
                SendLocalMesssage(finalMessage);

            });*/

        }



    
        private void SendLocalMesssage(string message)
        {
            Device.InvokeOnMainThreadAsync(() =>
            {
                Messages.Add(new Message
                {
                    ServerMessage = message
                });

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

                Messages.Add(new Message
                {
                    ServerMessage = "Connected..."
                });
            }
            catch (Exception ex)
            {
                Messages.Add(new Message
                {
                    ServerMessage = $"Connected error:{ex.Message}"
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


        private Task SendMessage()
        {
            throw new NotImplementedException();
        }
    }
}
