document.addEventListener("DOMContentLoaded", () => {

    const menuBtn = document.getElementById("menu-toggle");
    const sidebar = document.querySelector(".sidebar");
    const overlay = document.querySelector(".sidebar-overlay");

    function openSidebar() {
        sidebar.classList.add("show");
    }

    function closeSidebar() {
        sidebar.classList.remove("show");
    }

    if (menuBtn) {
        menuBtn.addEventListener("click", () => {
            sidebar.classList.toggle("show");
        });
    }

    if (overlay) {
        overlay.addEventListener("click", closeSidebar);
    }

    window.addEventListener("resize", () => {
        if (window.innerWidth > 992) {
            closeSidebar();
        }
    });

});