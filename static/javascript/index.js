

document.getElementById("urlDownload").addEventListener("submit", async function (event) {

    event.preventDefault()

    let url = document.getElementById("urlInput").value;

    const formData = {
        ytLink: url
    }

    const response = await fetch('http://127.0.0.1:5000/downloadMP3', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(async response => {
        try {
            if (response.ok) {
                // Download the file from the server
                const blob = await response.blob(); // Get the response as a Blob (binary data)
                const url = window.URL.createObjectURL(blob); // Create a temporary URL for the Blob
                const a = document.createElement('a'); // Create an anchor element
                a.href = url;
                a.download = 'deinSong.mp3'; // TODO: Maybe make name dynamic. Get title from server and input it here
                document.body.appendChild(a); // Append the anchor to the DOM
                a.click(); // Trigger the download
                a.remove(); // Remove the anchor from the DOM
                window.URL.revokeObjectURL(url); // Clean up the object URL

                console.log("File downloaded successfully");
            } else {
                console.error("Failed to download the file:", response.statusText);
            }
        } catch (error) {
            console.log("An error occured", error);
        }
    })
})