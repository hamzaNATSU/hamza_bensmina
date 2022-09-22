from django.test import TestCase

# Create your tests here.


def checkCat(Catname):
    return ('<script>document.getElementById("products-'+Catname+'").classList.add("active"); </script>')

    
def checkCol(Col):
    return ('<script>document.getElementById("profile-tab-'+Col+'").classList.add("active"); \ndocument.getElementById("tab-'+Col+'").classList.add("active");  </script>')


def items_to_html(order):
    html_items = ''
    for item in order.orderitem_set.all():
        html_items += ' <tr> <td width="75%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 15px 10px 5px 10px;"> '+ item.product.PRDName +' | x' + str(item.quantity) +'</td><td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 15px 10px 5px 10px;">' + str(item.Variant) +' </td> <td width="25%" align="left" style="font-family: Open Sans, Helvetica, Arial, sans-serif; font-size: 16px; font-weight: 400; line-height: 24px; padding: 15px 10px 5px 10px;"> $' + str(item.product.PRDPrice) +' </td> </tr>'
    return html_items