const firebaseConfig = {
    apiKey: "AIzaSyAZS1psgr7eUkr99KzOBrpGhvjT6VJu4Qo",
    authDomain: "nocturnal-b986b.firebaseapp.com",
    projectId: "nocturnal-b986b",
    storageBucket: "nocturnal-b986b.appspot.com",
    messagingSenderId: "489950292251",
    appId: "1:489950292251:web:3b1d4a23fd1c7a8f9c4bbe",
    measurementId: "G-1PNWDBZFD5"
  };

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();

// Reference to the Firebase Authentication
var auth = firebase.auth();
document.getElementById('register').addEventListener('click', signUp());

// Sign-up function
function signUp() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    auth.createUserWithEmailAndPassword(email, password)
    .then(function(user) {
                    console.log("User created with UID:", user.user.uid);
                    alert('User created')
                })
    .catch(function(error) {
                    console.error("Error creating user:", error);
                    alert('user not created')
                });
    }

    function signIn() {
        var email = document.getElementById("email").value;
        var password = document.getElementById("password").value;

        auth.signInWithEmailAndPassword(email, password)
        .then(function(user) {
                console.log("User signed in with UID:", user.user.uid);
            })
        .catch(function(error) {
                console.error("Error signing in:", error);
            });
        }    

