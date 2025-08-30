let sucssesBtn = document.querySelector('.sucsses-btn')
sucssesBtn.addEventListener('click', () => {
  localStorage.removeItem("arrayProduct")
  localStorage.removeItem("arrayProductCount")
  localStorage.removeItem("arrayProductPrice")
  localStorage.removeItem("arrayProductImg")
    
})