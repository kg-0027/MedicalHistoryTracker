document.addEventListener("DOMContentLoaded", () => {
    var addButton = document.querySelector('.update-button');
    var popup = document.getElementById('popup');
    var closeBtn = document.getElementById('close');
    
    addButton.addEventListener("click", () => {
      popup.style.display = 'block';
    });
  
    closeBtn.addEventListener('click', function() {
      popup.style.display = 'none';
    });
  
    document.addEventListener('click', function(event) {
      if (event.target == popup) {
        popup.style.display = 'none';
      }
    });
  
    document.getElementById('save-button').addEventListener('click', function() {
      var medicine = document.getElementById('medicine-update').value;
      var quantity = document.getElementById('quantity-update').value;
      var expiryDate = document.getElementById('expiry-date-update').value;
      var status = document.getElementById('status-update').value;
      
      // Create the popup content
      var popupContent = '<p>Medicine: ' + medicine + '</p>' +
                         '<p>Quantity: ' + quantity + '</p>' +
                         '<p>Expiry Date: ' + expiryDate + '</p>' +
                         '<p>Status: ' + status + '</p>';
      
      // Update the popup content
      var popupContentDiv = popup.querySelector('.popup-content');
      popupContentDiv.innerHTML = popupContent;
    });
  });
  