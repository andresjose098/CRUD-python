



export const getGifs = async (category) => {
    const url = `https://api.giphy.com/v1/gifs/search?q=${encodeURI (category)}&limit=10&api_key=wW04qnayXXOz6SmNritauosn5YYk323N`;
    try {
        const resp = await fetch(url);
        if (!resp.ok) {
            throw new Error(`HTTP error! status: ${resp.status}`);
        }
        const {data} = await resp.json();
        
        const gifs= data.map( img =>{
            return{
                id: img.id,
                tittle: img.title,
                url: img.images?.downsized_medium.url
            }
        })

        return gifs;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};
