var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Enable serving static files from wwwroot
app.UseDefaultFiles(); // Serves index.html by default
app.UseStaticFiles();

// Keep API endpoint available at /api/hello
app.MapGet("/api/hello", () => "Hello World!");

app.Run();
