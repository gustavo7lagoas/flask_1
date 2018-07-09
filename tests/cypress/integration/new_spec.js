context('New Game', () => {
    Cypress.Commands.add('gameLibraryLogin', () => {
        cy.request({
            method: 'POST',
            url: '/authenticate',
            form: true,
            body: {
                next: '/',
                username: 'test',
                passwd: 'mestra',
            }
        })    
    })
    it('redirects to login when does not have a session', () => {
        cy.visit('/new')
            .url()
            .should('contain', '/login')
    })
    it('should open form when have a session', () => {
        cy.gameLibraryLogin()
        cy.getCookie('session').should('exist')
        cy.visit('/new')
        cy.get('.page-header h1')
            .should('contain', 'New Game')
    })
    it('should add a new game to library', () => {
        cy.gameLibraryLogin()
        cy.visit('/new')
        cy.get('[data-cy="name"]')
            .type('Super Star Soccer')
            .get('[data-cy="category"]')
            .type('Sports')
            .get('[data-cy="game_console"]')
            .type('Snes')
            .get('[data-cy="save"]')
            .click()
        cy.get('[data-cy="game-library"] tr')
            .should('have.length', 5)
            .should('contain', 'Super Star')
    })
})
