var config = {
  apiKey: "AIzaSyDGrtyTaEJAaf57_mQxlSFO2udmVKEDkBk",
  authDomain: "event-database-7c8d5.firebaseapp.com",
  databaseURL: "https://event-database-7c8d5.firebaseio.com",
  storageBucket: "event-database-7c8d5.appspot.com",
  messagingSenderId: "453722478637"
};
firebase.initializeApp(config);

var ref = firebase.database().ref("events/");

function post_event(event_data) {
  $('#events').append(
    '<div class="event">' +
    '<h2 class="title">' + event_data.title + '</h2>' +
    '<p class="date">' + event_data.date + '</p>' +
    '<p class="description">' + event_data.description + '</p>' +
    '</div>'
  );
}

function load_events() {
  ref.orderByKey().once('value')
  .then(function(dataSnapshot) {
    var data = dataSnapshot.val();
    for(var key in data) {
      post_event(data[key]);
    }
  });
}

$(document).ready(function() {
  load_events();
})