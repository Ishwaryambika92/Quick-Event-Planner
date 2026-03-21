document.addEventListener("DOMContentLoaded", function () {
    console.log("Quick Event JS Loaded!");
    // You can add cool JS effects or interactions here later
    function toggleDarkMode() {
        document.body.classList.toggle('bg-dark');
        document.body.classList.toggle('text-white');
        localStorage.setItem('darkMode', document.body.classList.contains('bg-dark'));
    }
    
    window.onload = () => {
        if (localStorage.getItem('darkMode') === 'true') {
            document.body.classList.add('bg-dark', 'text-white');
        }
    }
    
});
