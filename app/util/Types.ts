
export type RecipeItem = {
    name: string 
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
    
    imageUrl: string 
    method: {
        step: number
        text: string | null
    }[] | null
}