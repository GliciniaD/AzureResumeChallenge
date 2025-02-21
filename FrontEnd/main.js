//Given the fact that HTML has already been uploaded, I'll just embed the javascript below within the HTML file rather than upload js file

window.addEventListener('DOMContentLoaded', () => {
    getVisitorCount(); // Call function when the page loads
});

const functionApi = "https://functionforapichunk28494.azurewebsites.net/api/updatecounter/global_visitor_count?code=TVdo3unWgaEdIrp9iRASwDtZNB4F7MV2jVMvmbzw3hf7AzFupP2rMA=="; // Replace with your actual API endpoint

const getVisitorCount = () => {
    fetch(functionApi)
        .then(response => response.json()) // Convert API response to JSON
        .then(data => {
            console.log("Visitor count retrieved:", data.visitCount); // Access visitCount instead of count
            document.getElementById("counter").innerText = data.visitCount; // Display the correct count
        })
        .catch(error => {
            console.error("Error fetching visitor count:", error);
            document.getElementById("counter").innerText = "Error loading count";
        });
};

