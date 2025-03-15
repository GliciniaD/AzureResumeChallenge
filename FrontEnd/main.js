window.addEventListener('DOMContentLoaded', () => {
    getVisitorCount(); // Call function when the page loads
});

const functionApi ='https://visitorcountapim.azure-api.net/visitor-count/updatecounter/global_visitor_count '

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

