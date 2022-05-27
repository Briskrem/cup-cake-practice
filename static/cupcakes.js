const cupCakeList = $('.cupcake-list')
$('.get-list').on('click', get_cupcakes)



async function get_cupcakes(){
    cupCakeList.empty()
    cupcakes = await axios.get('/api/cupcakes')
    console.log(cupcakes)
    console.log(cupcakes.data.cupcakes)
    cupcakes.data.cupcakes.forEach(cupcake => {
        const $cake = generateMarkup(cupcake)
        cupCakeList.append($cake)
    })
    $('.dd').on('click', deleteCupcake)
}

function generateMarkup(cupcake){

    return $(`
        <li class="row justify-content-center  gg" data-id="${cupcake.id}" style="border:2px solid">
            <div>
                <div>
                <img src="${cupcake.image}" alt="" width="150px" height="150px" >
                </div>
                <p class="">${cupcake.flavor}</p>
                <p class="">${cupcake.size}</p>
                <p class="">${cupcake.rating}</p>
                <button class='dd'>DELETE</button>
            </div>
           
        </li>
    `)
}

$('.subby').on('click', postCupCakes)

async function postCupCakes(e){
    e.preventDefault()
    const $flavor = $('#flavor').val()
    const $size = $('#size').val()
    const $rating = $('#rating').val()
    const $image = $('#image').val()
    console.log(`HERE IT IS : ${$flavor} , ${$size}, ${$rating}, ${$image}`)
    posted = await axios({
        url: '/api/cupcakes',
        method: 'POST',
        data: {flavor: $flavor, size: $size, rating: $rating, image:$image}
    })
    console.log(posted)
}





async function deleteCupcake(e){
    e.preventDefault()
    console.dir(e.target)
    let cup_cake = $(e.target).closest('li')
    cupcakeID = cup_cake.attr("data-id")
    console.log(cupcakeID)
    const deleted = await axios({
        url: `/api/cupcakes/${cupcakeID}`,
        method: 'DELETE',
    })
    console.log(deleted)
    cup_cake.remove();
}