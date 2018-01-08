function initAutocomplete() {
  // initmap
    // Add autocomplete function to searchbox
  var input = $('.search-box');
  for (i = 0; i < input.length; i++) {
    autocomplete = new google.maps.places.Autocomplete(input[i]);
  };
}
