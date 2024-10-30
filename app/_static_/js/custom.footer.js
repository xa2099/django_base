function themeUse(url)
{
    localStorage.setItem('userTheme', url);
    document.getElementById("cssLink").href = url;
}

function buildThemeModeSelector()
{
    let themeMenu = document.querySelector('#theme-menu');
    if (!themeMenu) return;
    document.querySelectorAll('[data-bs-theme-value]').forEach(value => {
        value.addEventListener('click', () => {
            const theme = value.getAttribute('data-bs-theme-value');
            document.documentElement.setAttribute('data-bs-theme', theme);
            localStorage.setItem('themeMode', theme);
        });
    });
}

buildThemeModeSelector();
