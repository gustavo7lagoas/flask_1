context('New Game', () => {
    it('redirects to login when does not have a session', () => {
        cy.visit('/new')
            .url()
            .should('contain', '/login')
    })
    it.only('should open form when have a session', () => {
        cy.request({
            method: 'POST',
            url: '/authenticate',
            body: {
                username: 'test',
                passwd: 'mestra',
            }
        })
        cy.visit('new')
            .debug()
    })
})
