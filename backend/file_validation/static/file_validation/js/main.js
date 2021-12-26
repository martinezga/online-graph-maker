$(document).ready( function () {
    let table = $('#table').DataTable({
      ordering:  false,
    });
    $( table.table().container() )
    .addClass('table-responsive' );
  } );