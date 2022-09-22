var updateBtns = document.getElementsByClassName('update-cart');
var variantbtn = document.getElementById('update-variant');
var variant;
function update_variant(Variant)
{
    variant = Variant;
}
for (var i = 0 ; i<updateBtns.length; i++){
updateBtns[i].addEventListener('click' , function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId : ', productId , 'action:', action)
    console.log('variant :',variant);

    
    console.log('USER :' , user)
    if (user === 'AnonymousUser'){
        console.log('Not logged in')
    }
    else{
        updateUserOrder(productId, action, variant)
    
    }
})
}
function updateUserOrder(productId, action,variant){
    console.log('User is logged in ...')
    const url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({
            'productId':productId,
            'action':action,
            'variant':variant,
        }),  

    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data :', data)
    })
}
var i=0;
function fav_defav(){
    if (document.getElementById('fav-button').data-action == 'defavorite'){
        document.getElementById('fav-button').setAttribute('data-action','favorite');
        console.log(document.getElementById('fav-button').data-action)
    }
    else {
        document.getElementById('fav-button').setAttribute('data-action','defavorite');
        console.log(document.getElementById('fav-button').data-action)

    }

}