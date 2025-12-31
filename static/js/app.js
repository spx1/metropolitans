// this function will determine a form's holding container
    function get_holding_container(elem) {
    for( div of document.getElementsByTagName('div') ) {
        if( div.contains( elem ) ) {
            return div;
        }
    }
    return null;
}
        
function toggle_vendor_form(id)
{
    var form = document.getElementById(id);
    var container = get_holding_container(form);
    if( container != null ) {
        if( container.style.display == 'none' || container.style.display == '') {
            container.style.display = 'block';
        } else {
            container.style.display = 'none';
        }
    }
}