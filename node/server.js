//Name: Joseph Svintsitsky
//Module: Lab 6
//Due Date: 10/10/2021
//Assignment: Create a Node web server and display the following data:
//In addition to the hostname and IP as shown above, 
//add in the server uptime (in Days, Hours, Minutes, Seconds), 
//Total Memory in MB, Free Memory in MB, and Number of CPUs.
//Resources: https://www.geeksforgeeks.org/ and Professor AJ Bothe

// Node JS modules to extract data
var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

function uptime(){

  //Calculate the uptime by doing conversions from secs,mins,hours, and days
  var ut_sec = os.uptime();
  var ut_min = ut_sec/60;
  var ut_hour = ut_min/60;
  var ut_day = ut_hour/24;
     
  ut_sec = Math.floor(ut_sec);
  ut_min = Math.floor(ut_min);
  ut_hour = Math.floor(ut_hour);
  ut_day = Math.floor(ut_day);
    
  ut_hour = ut_hour%60;
  ut_min = ut_min%60;
  ut_sec = ut_sec%60;
  ut_day = ut_day%24;

  return ut_day + " Days , " + ut_hour + " Hours , " + ut_min + " minutes and " + ut_sec + " seconds "
}

function totalmem(){
  
  //Calculate the total memory of the system running the script 
  //and doing conversions to get an accurate storage size
  var total_memory = os.totalmem();
  var total_mem_in_kb = total_memory/1024;
  var total_mem_in_mb = total_mem_in_kb/1024;
   
  total_mem_in_kb = Math.floor(total_mem_in_kb);
  total_mem_in_mb = Math.floor(total_mem_in_mb);
   
  total_mem_in_mb = total_mem_in_mb%1024;
  total_mem_in_kb = total_mem_in_kb%1024;
  total_memory = total_memory%1024;
  
    return  total_mem_in_mb + "MB ";
}

function freemem(){

  //Calculate how much free memory is on the users drive by doing conversions
  var free_memory = os.freemem();
  var free_mem_in_kb = free_memory/1024;
  var free_mem_in_mb = free_mem_in_kb/1024;
  var free_mem_in_gb = free_mem_in_mb/1024;
   
  free_mem_in_kb = Math.floor(free_mem_in_kb);
  free_mem_in_mb = Math.floor(free_mem_in_mb);
  free_mem_in_gb = Math.floor(free_mem_in_gb);
   
  free_mem_in_mb = free_mem_in_mb%1024;
  free_mem_in_kb = free_mem_in_kb%1024;
  free_memory = free_memory%1024;

    return free_mem_in_mb + "MB";
}

function numofcpu(){

  //Reads the system info to see how many cpus and cores the users machine has
  var cpu_s=os.cpus();
  var no_of_logical_core=0;
  cpu_s.forEach(element => { 
  no_of_logical_core++;

}); 
    return no_of_logical_core;
}

//Creates a connection to the localhost server and displays the functions return values in html format
http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${uptime()} </p>
            <p>Total Memory: ${totalmem()} </p>
            <p>Free Memory: ${freemem()} </p>
            <p>Number of CPUs: ${numofcpu()} </p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
