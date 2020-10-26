const form = document.getElementById("submitForm")
const textInput = document.getElementById("textInput")


function navigateToSearch(e) {

    window.location.replace(`/search/by-category/${textInput.value}`);
    e.preventDefault()
}


form.addEventListener("submit", navigateToSearch)
