// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyAM3hjrsZzU2rEjjEAsaY-LebpdS-dDuOA",
    authDomain: "bumper-6a073.firebaseapp.com",
    databaseURL: "https://bumper-6a073.firebaseio.com",
    projectId: "bumper-6a073",
    storageBucket: "bumper-6a073.appspot.com",
    messagingSenderId: "617314005412",
    appId: "1:617314005412:web:76b17eb7cb5474f6929131",
    measurementId: "G-EBKWBZQH2S"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
firebase.analytics();
var ui = new firebaseui.auth.AuthUI(firebase.auth());
var uiConfig = {
    callbacks: {
        signInSuccessWithAuthResult: function(authResult, redirectUrl) {
            // User successfully signed in.
            // Return type determines whether we continue the redirect automatically
            // or whether we leave that to developer to handle.
            return true;
        },
        uiShown: function() {
            // The widget is rendered.
            // Hide the loader.
            document.getElementById('loader').style.display = 'none';
        }
    },
    // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
    signInFlow: 'popup',
    signInSuccessUrl: 'home',
    signInOptions: [
        // Leave the lines as is for the providers you want to offer your users.
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
    ]
};
ui.start('#firebaseui-auth-container', uiConfig);