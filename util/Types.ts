
export type RecipeItem = {
    name: string, 
    prep_time: string | null,
    cook_time: string | null,
    ingredients: 
        {
            name: string | null,
            quantity: {
                quantity: number | null | string
                unit: string | null
            } | null ,
            notes: string | null
        }[]
    
    image_url: string 
    method: {
        step: number
        text: string | null
    }[] | null
}

export type Grocery = {
    brand: string,
    name: string,
    list_price: string,
    unit_price: {
        price: number,
        quantity: number,
        unit: string,
    },
    image_url: string,
    unit_size: string
}