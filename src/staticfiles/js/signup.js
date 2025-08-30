const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

const signUpButton2 = document.getElementById('signUp2');
const signInButton2 = document.getElementById('signIn2');

signUpButton2.addEventListener('click', () => {
	container.classList.add("right-panel-active");
  console.log('signUpButton2 clicked');
  
});

signInButton2.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});