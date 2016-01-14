function insertChar(char)
{
    document.getElementById("search-bar").value = document.getElementById("search-bar").value + char;
    document.getElementById("search-bar").focus();
    return document.getElementById("search-bar").value;
}

function updateURL(query)
{
  document.getElementById("search-form").action = "/search/" + query;
}

function switchLangs(switch_to)
{
  if (switch_to == 'esp') {
    document.getElementById('english_to_esperanto').className = 'unselected-lang';
    document.getElementById('esperanto_to_english').className = 'selected-lang';
    document.getElementById('lang_spec_esp_to_eng').className = 'selected-lang-spec';
    document.getElementById('lang_spec_eng_to_esp').className = 'unselected-lang-spec';
  } else {
    document.getElementById('english_to_esperanto').className = 'selected-lang';
    document.getElementById('esperanto_to_english').className = 'unselected-lang';
    document.getElementById('lang_spec_esp_to_eng').className = 'unselected-lang-spec';
    document.getElementById('lang_spec_eng_to_esp').className = 'selected-lang-spec';
  }

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
