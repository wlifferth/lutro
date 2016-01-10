function insertChar(char)
{
    document.getElementById("search-bar").value = document.getElementById("search-bar").value + char;
    document.getElementById("search-bar").focus();
    return document.getElementById("search-bar").value;
}

function otterSwim()
{
  otter = document.getElementById("otter");
  var right = -200;
  var speed = 1;
  function updateFrame()
  {
    if(right % 30 == 0)
    {
      speed = (speed + 1) % 3 + 1;
    }
    right = right + speed;
    otter.style.right = right + 'px';

    if (right >= screen.width)
    {
      right = -200;
    }
  }
  var id = setInterval(updateFrame, 30);

}
