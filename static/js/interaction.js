function insertChar(char)
{
    document.getElementById("search-bar").value = document.getElementById("search-bar").value + char;
    document.getElementById("search-bar").focus();
    return document.getElementById("search-bar").value;
}
