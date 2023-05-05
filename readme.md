# **STILL IN PRODUCTION**

references:
https://css-tricks.com/css-only-carousel/


main {
    @include flexCenter(row);
    width: 80%;
    margin: 0 auto;
    
    #{&}__paragraph {
        font-weight: weight(bold);

        &:hover { 
            color: pink;
        }
    }
}

@mixin <function name>($<parameter name>){
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

to do:
create arrow button in javascript to go through each section of horizontal page


