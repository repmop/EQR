var count = 3;
function removebutton(){
    var elem = document.getElementById('button');
    elem.parentNode.removeChild(elem);
}
function addrow(){
    row = `<div class="row"><div class="inputfield col s12 m4 l3"><input id="Component Value`;
    row += count;
    row += `" type="text" class="validate" name="Component Value`;
    row += count;
    row += `"><label for="Component Value`;
    row += count;
    row += `">Component Value</label></div><div class="inputfield col s12 m7 l5"><input id="Quantity`;
    row += count;
    row += `" type="text" class="validate" name=Quantity`;
    row += count;
    row += `><label for="Quantity`;
    row += count;
    row += `">Quantity</label></div><div class="inputfield col s12 m11 l3">`;
    row += `</div><div id="button">
                    <div class="col s12 m1 l1 right-align">
                    <a onclick="removebutton();addrow()" class="btn-floating btn-large waves-effect waves-light red"><i class="material-icons">add</i></a>
                    </div>
                </div>`;
    $("#newrows").append (row);
    count++;
};
