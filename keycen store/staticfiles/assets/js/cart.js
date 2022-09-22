var updateBtns = document.getElementsByClassName('update-cart');
var variantbtn = document.getElementById('update-variant');
var variant;

// function update_variant(Variant)
// {
//     variant = Variant;
// }
for (var i = 0 ; i<updateBtns.length; i++){
updateBtns[i].addEventListener('click' , function(){
    if (qnt == undefined){
        qnt = 1;
    }
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log('quantity:',qnt);
    console.log('productId : ', productId , 'action:', action);
    console.log('quantity :',qnt);
    console.log('csrftoken :',csrftoken);
    console.log('device',device)
    updateUserOrder(productId, action, qnt);
});
}

function updateUserOrder(productId, action,qnt){
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
            'quantity':qnt,
        }),
        credentials: "same-origin",
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        document.getElementById('checkout'+productId).style.opacity = '1';
        document.getElementById('checkout'+productId).style.marginLeft = '50%';

    })
}