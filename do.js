(
    async function () {
        const response = await fetch('http://localhost:5000/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                'question': "hello bro!"
            })
        });
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        
        const data = await response.json();
        console.log(typeof (data['answer']));        
        console.log((data['answer']));
        data = JSON.parse(data['answer']);
        
        
    } ()
)
