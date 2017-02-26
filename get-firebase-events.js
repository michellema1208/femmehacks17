var config = {
  apiKey: "AIzaSyDGrtyTaEJAaf57_mQxlSFO2udmVKEDkBk",
  authDomain: "event-database-7c8d5.firebaseapp.com",
  databaseURL: "https://event-database-7c8d5.firebaseio.com",
  storageBucket: "event-database-7c8d5.appspot.com",
  messagingSenderId: "453722478637"
};
firebase.initializeApp(config);

var EVENTS_PER_PAGE = 5;

var current_page = 2;
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

function load_events(first, last) {
  ref.orderByChild('priority').startAt(first).endAt(last).once('value')
  .then(function(dataSnapshot) {
    var data = dataSnapshot.val();
    for(var key in data) {
      post_event(data[key]);
    }
  });
}

function load_buttons(){
  
}

function load_data() {
  var first = current_page * EVENTS_PER_PAGE;
  var last = (current_page*EVENTS_PER_PAGE) + (EVENTS_PER_PAGE - 1);
  load_events(first, last);
  load_buttons();
}

function next_page(){
  $('#events').html('');
  current_page++;
  load_data();
}

function previous_page() {
  $('#events').html('');
  current_page--;
  load_data();
}



$(document).ready(function() {
  load_data();
})
