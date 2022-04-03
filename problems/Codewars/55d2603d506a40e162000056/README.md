[_metadata_:generated]: - "true"

# Reducing Problems - Bug Fixing #8

<!-- INFO TABLE BEGIN -->

| Provider                                        | Source                                                                               | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| :---------------------------------------------: | :----------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [Codewars](../../../docs/providers/Codewars.md) | [`55d2603d506a40e162000056`](https://www.codewars.com/kata/55d2603d506a40e162000056) | [<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924087/python_xzdlti.svg" alt="Python" title="Python" width="50" />](solve.py)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924076/javascript_ehszr7.svg" alt="JavaScript" title="JavaScript" width="50" />](solve.js)[<img src="https://res.cloudinary.com/rascaltwo/image/upload/v1631924090/ruby_v4klwh.svg" alt="Ruby" title="Ruby" width="50" />](solve.rb) |

<!-- INFO TABLE END -->

<h1>Reducing Problems - Bug Fixing #8</h1>
<p>
Oh no! Timmy's reduce is causing problems, Timmy's goal is to calculate the two teams scores and return the winner but timmy has gotten confused and sometimes teams don't enter their scores, total the scores out of 3! Help timmy fix his program!

Return true if team 1 wins or false if team 2 wins!
</p>

<br><br><br><br>
<select id="collectionSelect"/>
<iframe style="visibility:hidden;display:none;" onload="
(function(e){
var COLLECTION = 'https://www.codewars.com/collections/bug-fixing';
var qCode = String.fromCharCode(34);
function ioa(str, f) {
  var a=[],i=-1;
  while((i=str.indexOf(f,i+1)) >= 0) a.push(i);
  return a;
}

function fc(op,cl) {
  var arr=[], d=0;
  op = op.map(a => {return {i:a,q:'<'};});
  cl = cl.map(a => {return {i:a,q:'>'};});
  var cmb = [].concat(op,cl).sort((a,b) =>a.i-b.i);
  for(var i=0;i<cmb.length-1;i++) {
    d += cmb[i].q === '<' ? 1 : -1;
    if(d === 0 || (i > 2 && d === 2))
      return cmb[i].i;
  }
  return -1;
}

function processKataData(data) {
  var kataData = {};
  var inx1 = data.indexOf('data-title='+qCode)+12;
  var kataTitle = data.slice(inx1).slice(0,data.slice(inx1).indexOf(qCode))
  
  var inx2 = data.indexOf('href='+qCode)+6;
  var kataLink = data.slice(inx2).slice(0,data.slice(inx2).indexOf(qCode))
  
  kataData.title = kataTitle;
  kataData.link = kataLink;
  
  return kataData;
}

function processData(msg) {
   var data = msg.split('\n');
    var dindex = data.slice(7,8).join('').indexOf('<div class='+qCode+'nine columns prn'+qCode+'>');
      var filteredData = data.slice(7,8).join('').split('').filter((a,i) => i>=dindex).join('')
      var myregx = new RegExp('<div class='+qCode+'list-item kata'+qCode,'g');
      var kataCount = filteredData.match(myregx).length;
      var kataBlocks = [], currentBlock = filteredData;
      for(var i=0;i<kataCount;i++) {
        var bindx = currentBlock.indexOf('<div class='+qCode+'list-item kata'+qCode+''), 
        block = currentBlock.slice(bindx),
        closingBlock = fc(ioa(block, '<div').slice(0,10),ioa(block, '</div').slice(0,10)),
        kataData = block.slice(0,closingBlock).replace(/(<)/g,'[').replace(/(>)/g,']');
        kataBlocks.push(kataData);
        currentBlock = block.slice(closingBlock+3);
      }
      var kataDatas = kataBlocks.map(processKataData);
      return kataDatas;
}

function getData() {
  $.ajax({ 
    type: 'GET',
    url: COLLECTION,
    headers: {
      Host: 'www.codewars.com',
      Accept: 'text/html, */*; q=0.01',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'X-PJAX': 'true',
      'X-PJAX-Container': 'body',
      'X-Requested-With': 'XMLHttpRequest',
      Referer: 'https://www.codewars.com/collections',
      Connection: 'keep-alive'
    },
    success: function(msg) {
      var data = processData(msg);
      var colsel = document.getElementById('collectionSelect');
      for(var i=0;i<data.length;i++) {
        var option = document.createElement('option');
        option.text = data[i].title;
        option.value = data[i].link
        colsel.add(option);
      }
      
      function onchanging(e) {
        alert(e);
      }
      
      colsel.addEventListener(
         'change',
         function(e) {
           var options = colsel.options;
           if(colsel.selectedIndex < options.length) {
             var selected = options[colsel.selectedIndex];
             if(selected) {
               console.log(selected.value);
               window.location.href = 'https://www.codewars.com' + selected.value;
             }
           }
         },
         false
      );
    }
  });
}
getData();
})(this)" />
