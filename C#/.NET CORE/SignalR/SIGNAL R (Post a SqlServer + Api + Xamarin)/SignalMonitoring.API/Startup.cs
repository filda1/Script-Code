using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using Microsoft.Extensions.Options;
using SignalMonitoring.API.Hubs;
using SignalMonitoring.API.Persistence;
using SignalMonitoring.API.Services;

namespace SignalMonitoring.API
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddMvc().SetCompatibilityVersion(CompatibilityVersion.Version_2_2);
            services.AddDbContext<MainDbContext>(contextOptions =>
            {
                contextOptions.UseSqlServer(Configuration.GetValue<string>(key: "ConnectionString"));
            });

            services.AddTransient<ISignalService, SignalService>();

            services.AddSignalR();
           /* services.AddCors(o => o.AddPolicy("CorsPolicy", builder =>
            {
                builder
                .AllowAnyMethod()
                .AllowAnyHeader()
                .AllowCredentials()
                .WithOrigins("http://localhost:4200");
            }));*/
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IHostingEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            //cors configured
            //app.UseCors("CorsPolicy"); 

            //signalR service configured
            app.UseSignalR(routes =>
            {
                routes.MapHub<SignalHub>("/signalHub");
            });


            app.UseMvc();
        }
    }
}
