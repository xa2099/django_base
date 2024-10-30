const userMode = localStorage.getItem('themeMode');
if (userMode) {
    document.documentElement.setAttribute('data-bs-theme', userMode);
}

const userTheme = localStorage.getItem('userTheme');
if (userTheme) {
    document.getElementById("cssLink").href = userTheme;
}
