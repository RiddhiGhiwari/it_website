document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contactForm');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();
        
        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            email: formData.get('email'),
            phone: formData.get('phone'),
            message: formData.get('message'),
        };

  
            const response = await fetch('http://127.0.0.1:8000/contact/save_contact/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                alert('Thank you for your message!');
                location.reload();
                const result = await response.json();
                // alert('Thank you for your message!');
               
            } else {
                const errorData = await response.json();
                alert('There was an error: ' + JSON.stringify(errorData));
            }
        
    });
});